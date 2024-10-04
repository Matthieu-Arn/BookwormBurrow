const editButtons = document.getElementsByClassName("btn-edit");
const bookreviewText = document.getElementById("id_reviewcontent");
const bookreviewForm = document.getElementById("bookreviewForm");
const submitButton = document.getElementById("submitButton");

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