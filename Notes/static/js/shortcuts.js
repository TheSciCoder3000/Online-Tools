window.onkeydown = function(e){
  if (e.which == 17){
    window.ctrl_pressed = true;
  }
  if (e.ctrlKey && e.which == 66){// Bold HK
    bold_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 83){// Bold HK
    save_changes();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 73 && !(e.shiftKey)){// Italic HK
    italic_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 85){// Underline HK
    underline_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 72){// Highlight HK
    highlight_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.altKey && e.which == 68){// Delete column
    e.preventDefault();
    delete_cell();
  }
  if (e.ctrlKey && e.shiftKey && e.which == 82) {// Add row
    e.preventDefault();
    add_row();
  }
  if (e.ctrlKey && e.shiftKey && e.which == 67) {//Add Column
    e.preventDefault();
    add_column();
  }
  if (e.which == 65) {//Add File
    let selected_objs = document.querySelectorAll('.obj-selected')
    let active_forms = document.querySelectorAll('.active-form')
    for (var i = 0; i < active_forms.length; i++) {
      active_forms[i].classList.remove("active-form")
      active_forms[i].style.display = 'none';
    }
    for (var i = 0; i < selected_objs.length; i++) {
      if (selected_objs[i].getAttribute("type") == "Folder"){
        console.log(selected_objs[i]);
        document.querySelector("#modal-container").style.display = "block"
        document.querySelector("#modal-text").innerText = "new Note"
        document.getElementById("File_name").classList.add("active-form")
        document.getElementById("File_name").style.display = "block";
        document.querySelector("#modal-form-btn").setAttribute("rootFolder", selected_objs[i].getAttribute("id"))
        document.querySelector("#modal-form-btn").setAttribute("obj-type", 'File')
      }
    }
  }
  if (e.shiftKey && e.which == 65) {//Add Folder
    let selected_objs = document.querySelectorAll('.obj-selected')
    let active_forms = document.querySelectorAll('.active-form')
    for (var i = 0; i < active_forms.length; i++) {
      active_forms[i].classList.remove("active-form")
      active_forms[i].style.display = 'none';
    }
    for (var i = 0; i < selected_objs.length; i++) {
      if (selected_objs[i].getAttribute("type") == "Folder"){
        console.log(selected_objs[i]);
        document.querySelector("#modal-container").style.display = "block"
        document.querySelector("#modal-text").innerText = "new Folder"
        document.getElementById("Folder_name").classList.add("active-form")
        document.getElementById("Folder_name").style.display = "block";
        document.querySelector("#modal-form-btn").setAttribute("rootFolder", selected_objs[i].getAttribute("id"))
        document.querySelector("#modal-form-btn").setAttribute("obj-type", 'Folder')
      }
    }
  }
  if (e.which == 46){//Delete Folder and Note
    var objects = document.querySelectorAll('.obj-selected');
    for (var i = 0; i < objects.length; i++) {
      let obj_type = objects[i].getAttribute("type")
      if (confirm(`Are you sure you want to delete this ${obj_type}`)) {
        let obj_name, root_id
        if (obj_type == "Folder") {
          obj_name = objects[i].getAttribute("foldername")
          root_id = objects[i].parentNode.parentNode.getAttribute("id")
          let obj_id = objects[i].getAttribute("id")
          if (sessionStorage.getItem("Openned Folders")){
            let opennedF = sessionStorage.getItem("Openned Folders").split(",")
            if (opennedF.includes(obj_id)) {
              let obj_index = opennedF.indexOf(obj_id);
              if (obj_index > -1) {
                opennedF.splice(obj_index, 1);
                sessionStorage.setItem("Openned Folders", opennedF)
              }
            }
          }
        } else {
          obj_name = objects[i].getAttribute("filename")
          root_id = objects[i].parentNode.parentNode.getAttribute("id")
        }
        if (objects[i].parentNode.getAttribute("id") == "rootF") {
          root_id = "root"
        }

        delete_obj(obj_type, root_id, obj_name)

      }
    }

    }
}

window.onkeyup = function (e){
  if (e.which == 17){
    window.ctrl_pressed = false;
  }
}
