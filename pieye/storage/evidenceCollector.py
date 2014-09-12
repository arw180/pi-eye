"""
Takes care of uploading all evidence to the cloud
"""


class EvidenceCollector:
    """
    Upload evidence
    """
    def __init__(self):
        self.unsavedEvidence = False
        pass

    def found_unsaved_evidence(self):
        """
        Are there files stored locally that have not been uploaded yet?
        """
        return self.unsavedEvidence
