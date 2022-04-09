# PDF Summary

Used to generate summary from text-based PDF file input

**URL**: `/pdfSummary`

**Method**: `POST`

**Auth required**: NO

**Input data format - Form data**

enctype: 'multipart/form-data'

```
input_file: [Text-based PDF file uploaded in the input]
```

**Constraints**

For the file being uploaded to the server, currently a limit of 1MB has been set as the max size. This can be configured during deployment in the code, and hence the max size is binding on the client. Any file larger than that will elicit an HTTP 413 response.

**Data example**

```
input_file: <great_depression.pdf>
```

## Success Response

**Code**: `200 OK`

**Content example**

```json
{
    "input": "The Great Depression was a severe worldwide economic depression that took place mostly...",
    "message": "Request complete",
	"status": "200",
	"summary": "The Great Depression was a severe worldwide economic depression that took place..."
}
```

## Error Responses

**Condition**: If "input_file" form field is missing from request.

**Code**: `400 BAD REQUEST`

**Content**:

```json
{
    "message": "File missing in request",
	"status": "400"
}
```

**Condition**: If no text can be extracted from the PDF

**Code**: `400 BAD REQUEST`

**Content**:

```json
{
    "message": "Could not extract any text from the file!",
	"status": "400"
}
```

**Condition**: If there's an error in processing the request

**Code**: `500 INTERNAL SERVER ERROR`

**Content**:

```json
{
    "message": "An error occured while processing your request",
	"status": "500"
}
```

**Condition**: If file size is larger than constraints of the API

**Code**: `413 PAYLOAD TOO LARGE`