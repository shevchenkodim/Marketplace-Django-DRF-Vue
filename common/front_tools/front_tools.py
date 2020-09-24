from django.db import models
from common.dictionaries.dictionaries import BackgroundColorDict, TextColorDict, TextSizeDict


class CustomizationOfAppearance(models.Model):
    """ Customization of appearance abstract models """
    bg_header = models.ForeignKey(BackgroundColorDict, on_delete=models.CASCADE, null=True, blank=True)
    text_header = models.ForeignKey(TextColorDict, on_delete=models.CASCADE, null=True, blank=True)
    text_size_header = models.ForeignKey(TextSizeDict, on_delete=models.CASCADE, null=True, blank=True)
    bg_body = models.ForeignKey(BackgroundColorDict, on_delete=models.CASCADE, null=True, blank=True)
    text_body = models.ForeignKey(TextColorDict, on_delete=models.CASCADE, null=True, blank=True)
    text_size_body = models.ForeignKey(TextSizeDict, on_delete=models.CASCADE, null=True, blank=True)
    text_for_link = models.ForeignKey(TextColorDict, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
