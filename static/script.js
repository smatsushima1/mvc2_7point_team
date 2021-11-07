function dev01() {
  var min = Math.ceil(0);
  var max = Math.floor(55);
  // First character
  do {
  		var rand = Math.floor(Math.random() * (max - min + 1)) + min;
	}
	while (rand == 35);
  // Second character  
  do {
  		var rand2 = Math.floor(Math.random() * (max - min + 1)) + min;
	}
	while (rand2 == 35 || rand2 == rand);
  // Third character
  do {
  		var rand3 = Math.floor(Math.random() * (max - min + 1)) + min;
	}
	while (rand3 == 35 || rand3 == rand2 || rand3 == rand);
  
  var char1 = document.getElementById('char1');
  var char2 = document.getElementById('char2');
  var char3 = document.getElementById('char3');
  // Do actions
  char1.innerHTML = rand;
  char2.innerHTML = rand2;
  char3.innerHTML = rand3;
}


