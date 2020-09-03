//list of keywords
const keywords_config = {
  '//list': true
}

function match(input, obj) {
  var matched = Object.keys(obj).find(key => input.toLowerCase().search(key) > -1);
  return obj[matched] || null;
}

function replace_template(id_num){
    return `
      <li id="list-${id_num}" class="list-type">
       My list
      </li>
    `
}

$(document).on('keydown', '.list-type', function (e){
  console.log('hello')
});

function setCaret(el) {
    var range = document.createRange()
    var sel = window.getSelection()

    range.setStart(el, 1)
    range.collapse(true)

    sel.removeAllRanges()
    sel.addRange(range)
}

$(document).on('keydown', '.cell-column', function (e){
  if (match(e.target.innerText, keywords_config)){
    console.log('option activated')
    var idN = document.querySelectorAll('.list-type').length
    e.target.innerHTML = e.target.innerHTML.replace('//list', replace_template(idN+1))

    var list_target = document.querySelector('#list-'+(idN+1)+' li')
    setCaret(list_target)
  }
});
