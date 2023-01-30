from django.forms.widgets import Textarea, RadioSelect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, UpdateView, DetailView

from colander.core.models import Event, EventType, Observable
from colander.core.views import get_active_case


class EventCreateView(CreateView):
    model = Event
    template_name = 'pages/collect/events.html'
    success_url = reverse_lazy('collect_event_create_view')
    fields = [
        'type',
        'name',
        'description',
        'first_seen',
        'last_seen',
        'count',
        'extracted_from',
        'observed_on',
        'detected_by',
        'involved_observables',
        'source_url',
        'tlp',
        'pap'
    ]

    def get_form(self, form_class=None):
        active_case = get_active_case(self.request)
        form = super(EventCreateView, self).get_form(form_class)
        event_types = EventType.objects.all()
        choices = [
            (t.id, mark_safe(f'<i class="nf {t.nf_icon} text-primary"></i> {t.name}'))
            for t in event_types
        ]
        form.fields['involved_observables'].widget.attrs = {'size': 30}
        form.fields['involved_observables'].queryset = Observable.get_user_observables(self.request.user, active_case)
        form.fields['type'].widget = RadioSelect(choices=choices)
        form.fields['description'].widget = Textarea(attrs={'rows': 2, 'cols': 20})
        return form

    def form_valid(self, form):
        active_case = get_active_case(self.request)
        if form.is_valid() and active_case:
            event = form.save(commit=False)
            event.owner = self.request.user
            event.case = active_case
            event.save()
            form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['events'] = Event.get_user_events(self.request.user, self.request.session.get('active_case'))
        ctx['is_editing'] = False
        return ctx


class EventUpdateView(EventCreateView, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['events'] = Event.get_user_events(self.request.user, self.request.session.get('active_case'))
        ctx['is_editing'] = True
        return ctx


class EventDetailsView(DetailView):
    model = Event
    template_name = 'pages/collect/event_details.html'
