import OnjiSimpleWizard from "./onji-simple-wizard.js";

const wizard = new OnjiSimpleWizard();

// first page
wizard.addPage(
  "First Page",
  () => { // on load event listener
    // store the data in wizard shared data
    wizard.setSharedDataForKey("data-from-first-page", "Hello World!");
  },
  "Back", () => wizard.viewPreviousPage(), // left button event listener
  "Next", () => wizard.viewNextPage() // right button event listener
);

// second page
wizard.addPage(
  "Second Page",
  () => { // on load event listener
    // get the data from the wizard shared data
    const dataFromFirstPage = wizard.getSharedDataForKey("data-from-first-page");
    console.log(dataFromFirstPage);
  },
  "Back", () => wizard.viewPreviousPage(), // left button event listener
  "Next", () => wizard.viewNextPage() // right button event listener
);

// third page
wizard.addPage(
  "Third Page",
  () => {}, // on load event listener
  "Back", () => wizard.viewPreviousPage(), // left button event listener
  "Finish", () => location.reload() // right button event listener, reload the page
);

wizard.showWizard();
