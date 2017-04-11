from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from whitenoise.storage import CompressedStaticFilesMixin
from pipeline.storage import PipelineMixin


class WhiteNoisePipelineStorage(CompressedStaticFilesMixin, PipelineMixin, ManifestStaticFilesStorage):
    pass
