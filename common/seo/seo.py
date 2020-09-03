from django.db import models


class SeoModel(models.Model):
    """" SEO abstract model """
    seo_title = models.CharField('Title', blank=True, max_length=100)
    seo_description = models.CharField('Description', blank=True, max_length=250)
    seo_keywords = models.CharField('Keywords', blank=True, max_length=250)

    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return ''

    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description
        return ''

    def get_seo_keywords(self):
        if self.seo_keywords:
            return self.seo_keywords
        return ''

    class Meta:
        abstract = True
