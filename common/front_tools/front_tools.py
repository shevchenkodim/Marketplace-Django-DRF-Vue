from django.db import models
from common.dictionaries.dictionaries import BackgroundColorDict, TextColorDict, TextSizeDict


class CustomizationOfAppearance(models.Model):
    """ Customization of appearance abstract models """
    bg_header = models.ForeignKey(BackgroundColorDict,
                                  on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='background color header+')
    text_header = models.ForeignKey(TextColorDict,
                                    on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='text color header+')
    text_size_header = models.ForeignKey(TextSizeDict,
                                         on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='text size header+')
    bg_body = models.ForeignKey(BackgroundColorDict,
                                on_delete=models.CASCADE, null=True, blank=True,
                                related_name='background color body+')
    text_body = models.ForeignKey(TextColorDict,
                                  on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='text color body+')
    text_size_body = models.ForeignKey(TextSizeDict,
                                       on_delete=models.CASCADE, null=True, blank=True,
                                       related_name='text size body+')
    text_for_link = models.ForeignKey(TextColorDict,
                                      on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='text color for link+')

    class Meta:
        abstract = True
