//PART 2
//TRAVERSING THE DOM //

var itemList = document.querySelector('#item');
console.log(itemList);

//parentNode
console.log(itemList.parentNode);
itemList.parentNode.style.backgroundColor = '#f4f4f4';
console.log(itemList.parentNode.parentNode.parentNode);

//parentElement
var itemList = document.querySelector('#item');
console.log(itemList.parentElement);
itemList.parentElement.style.backgroundColor = '#f4f4f4';
console.log(itemList.parentElement.parentElement.parentElement);

// childNodes
//console.log(itemList.childNodes);  // not recommend
console.log(itemList.children)

console.log(itemList.children[1])
itemList.children[1].style.backgroundColor='yellow'
itemList.children[1].textContent='children[1]'

//firstElementChild
console.log(itemList.firstElementChild)
itemList.firstElementChild.textContent = 'firstElementChild' 

//lastElementChild
console.log(itemList.lastElementChild)
itemList.lastElementChild.textContent = ' lastElementChild'

// nextSilbling
console.log(itemList.Silbling);
console.log(itemList.nextElementSilbling);

// previousSibling
console.log(itemList.previousSibling)
console.log(itemList.previousElementSibling)
itemList.previousElementSibling.style.color = 'red'

// createElement

// create a div
var newDiv = document.createElement('div')
// add class
newDiv.className = 'newDiv'
// add ID
newDiv.id = 'newDivID'
// add attr
newDiv.setAttribute('title','Hello Div')  //title="Hello Div"
// create text node
var newDivText = document.createTextNode('added by JavaScript ')
// add text to div
newDiv.appendChild(newDivText)

var container = document.querySelector('header .container')
var h1 = document.querySelector('header h1')

console.log(newDiv)
newDiv.style.fontSize = '20px'
container.insertBefore(newDiv,h1)
