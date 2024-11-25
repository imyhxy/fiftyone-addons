# Author: imyhxy
# File: cvat.py
# Date: 11/25/24
import fiftyone.core.metadata as fomt
import fiftyone.types as fot
import fiftyone.utils.cvat as fouc


class ExtendCVATImageDatasetImporter(fouc.CVATImageDatasetImporter):
    pass


class ExtendCVATImageDatasetExporter(fouc.CVATImageDatasetExporter):
    def export_sample(self, image_or_path, labels, metadata=None):
        out_image_path, uuid = self._media_exporter.export(image_or_path)

        # if labels is None:
        #     return  # unlabeled

        if not isinstance(labels, dict):
            labels = {"labels": labels}

        # if all(v is None for v in labels.values()):
        #     return  # unlabeled

        if metadata is None:
            metadata = fomt.ImageMetadata.build_for(image_or_path)

        if self.abs_paths:
            name = out_image_path
        else:
            name = uuid

        cvat_image = fouc.CVATImage.from_labels(labels, metadata)
        cvat_image.id = len(self._cvat_images)
        cvat_image.name = name

        self._cvat_images.append(cvat_image)


class ExtendCVATImageDataset(fot.CVATImageDataset):
    def get_dataset_importer_cls(self):
        return ExtendCVATImageDatasetImporter

    def get_dataset_exporter_cls(self):
        return ExtendCVATImageDatasetExporter
