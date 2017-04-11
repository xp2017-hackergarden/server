from django.contrib.staticfiles.storage import ManifestFilesMixin
from whitenoise.storage import CompressedStaticFilesMixin
from pipeline.storage import PipelineMixin


class WhiteNoisePipelineStorage(PipelineMixin, CompressedStaticFilesMixin, ManifestFilesMixin):
    pass
