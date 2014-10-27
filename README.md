s3etag
======

* A small Python script that calculates checksums on local files that should match AWS S3-calculated ETags.
* Intended for file upload integrity checking.
* If run from the command line, the first argument is the file name, second is optional chunksize for multipart uploads.
