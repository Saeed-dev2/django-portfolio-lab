from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        # Save the message
        contact_message = form.save()
        
        # Send email notification
        try:
            subject = f"New Contact Form Message: {form.cleaned_data['subject']}"
            message = f"""
            New message from your portfolio website:
            
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Subject: {form.cleaned_data['subject']}
            
            Message:
            {form.cleaned_data['message']}
            
            ---
            Sent from Portfolio Website Contact Form
            """
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            # Send confirmation email to sender
            confirmation_subject = "Thank you for contacting me!"
            confirmation_message = f"""
            Hi {form.cleaned_data['name']},
            
            Thank you for reaching out! I've received your message about "{form.cleaned_data['subject']}" and will get back to you as soon as possible.
            
            Best regards,
            [Your Name]
            """
            
            send_mail(
                confirmation_subject,
                confirmation_message,
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
                fail_silently=True,
            )
            
            messages.success(
                self.request, 
                'Thank you for your message! I will get back to you soon.'
            )
            
        except Exception as e:
            messages.error(
                self.request, 
                'There was an error sending your message. Please try again later.'
            )
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Please correct the errors below and try again.'
        )
        return super().form_invalid(form)