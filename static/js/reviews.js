const editButtons = document.getElementsByClassName("btn-edit");
const bookreviewText = document.getElementById("id_reviewcontent");
const bookreviewForm = document.getElementById("bookreviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated bookreview's ID upon click.
* - Fetches the content of the corresponding bookreview.
* - Populates the `bookreviewText` input/textarea with the bookreview's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_bookreview/{bookreviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookreviewId = e.target.getAttribute("bookreview_id");
    let bookreviewContent = document.getElementById(`bookreview${bookreviewId}`).innerText;
    bookreviewText.value = bookreviewContent;
    submitButton.innerText = "Update";
    bookreviewForm.setAttribute("action", `edit_bookreview/${bookreviewId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated bookreview's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific bookreview.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion of the bookreview.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookreviewId = e.target.getAttribute("bookreview_id");
      deleteConfirm.href = `delete_bookreview/${bookreviewId}`;
      deleteModal.show();
    });
  }