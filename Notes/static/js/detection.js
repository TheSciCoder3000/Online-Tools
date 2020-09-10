//list of keywords
const keywords_config = {
  '//list': 'list',
  '//check': 'checkbox',
  '//desc': 'description',
  '//num-list': 'numbered'
}

function match(input, obj) {
  var matched = Object.keys(obj).find(key => input.toLowerCase().search(key) > -1);
  return {key:matched, value:obj[matched]} || null;
}

function replace_template(id_num, key){
  switch (key){
    case 'list':
      return `
        <li id="list-${id_num}" class="list-type"></li>
      `
      break;
    case 'description':
      return `
        <li id="list-${id_num}" class="list-type desc-type">description</li>
      `
      break;
    case 'checkbox':
      return `
        <div class="list-type check-container">
          <div contenteditable="false" onclick="console.log('Clicked here true')">
            test
          </div>
          <span>Test</span>
        </div>
      `
      break;
    case 'numbered':
      return `
        <li id="list-${id_num}" class="list-type num-type"></li>
      `
      break;
  }
}

$(document).on('keydown', '.list-type', function (e){
  console.log('hello')
});

function setCaret(el) {
  var range = document.createRange()
  var sel = window.getSelection()

  range.setStart(el, 0)
  range.collapse(true)

  sel.removeAllRanges()
  sel.addRange(range)
  el.focus()
}

function try_nest_and_fail(keyword, template_tag){
  var lists = document.querySelectorAll("li")
  for (var i = 0; i < lists.length; i++) {
    if (lists[i].innerText.includes(keyword)) {
      var new_temp = `<ul class="m-0">${template_tag}</ul>`
      lists[i].innerHTML = lists[i].innerHTML.replace(keyword, new_temp)
      return false
      break;
    }
  }
  return true
}

$(document).on('keydown', '.cell-column', function (e){
  if (match(e.target.innerText, keywords_config).key){
    var keyW = match(e.target.innerText, keywords_config)
    var idN = document.querySelectorAll('.list-type').length
    if (try_nest_and_fail(keyW.key, replace_template(idN+1,keyW.value))){
      console.log('not nested');
      e.target.innerHTML = e.target.innerHTML.replace(keyW.key, replace_template(idN+1,keyW.value))
    }

    var list_target = document.querySelector('#list-'+(idN+1))
    console.log(e.target.innerHTML);
    setCaret(list_target)
    e.preventDefault();
  }
});
