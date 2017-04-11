from django.contrib.staticfiles.storage import ManifestFilesMixin
from whitenoise.storage import CompressedStaticFilesMixin
from pipeline.storage import PipelineMixin


class WhiteNoisePipelineStorage(CompressedStaticFilesMixin, PipelineMixin, ManifestFilesMixin):
    pass
