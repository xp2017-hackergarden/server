from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from whitenoise.storage import HelpfulExceptionMixin, CompressedStaticFilesMixin
from pipeline.storage import PipelineMixin


class WhiteNoisePipelineStorage(HelpfulExceptionMixin, CompressedStaticFilesMixin, PipelineMixin, ManifestStaticFilesStorage):
    pass
