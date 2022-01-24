from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    """
    Provides a user with the ability to renew a book that has been borrowed by
    modifying the due_back field. The new data must not be a past value and must not be
    more than 3 weeks into the future.

    Args:
        forms ([type]): [description]
    """ 
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks. (Default is 3)')  

    def clean_renewal_date(self):
        """A method for validating renewal date. The method must begin with 'clean_'
        """

        # self.cleaned_data is a django form for sanitizing inputs and removing any harmful
        # characters and also ensuring to return a properly defined data...ie date should be a
        # proper date.
        data = self.cleaned_data['renewal_date']

        # check if the renewal_date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date: Your renewal date is in the past.'))

        # check if the date is not more than 4 weeks in the future
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date: Date is more than 4 weeks ahead. Please choose a sooner date.'))
        
        # the cleaned data must always be returned
        return data