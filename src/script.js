// Generate first character
function genChar1() {
    // Establish criteria for random numbers
    var min = Math.ceil(0);
    var max = Math.floor(55);
    do {
       var first = Math.floor(Math.random() * (max - min + 1)) + min;
    }
    // Roll will never get picked
    while (first == 35);
    return first;
}


// Generate second character
function genChar2(chlist, id1, p1) {
    var min = Math.ceil(0);
    var max = Math.floor(55);
    do {
        var second = Math.floor(Math.random() * (max - min + 1)) + min;
        ch2p = chlist[second]['points']
    }
    // Must be less points than difference from first and 7
    while (second == 35 || second == id1 || ch2p >= 7 - p1);
    return second;
}


// Generate third character
function genChar3(chlist, id1, p1, id2, p2, max_ind) {
    var min = Math.ceil(0);
    var max = Math.floor(55);
    // When max_ind == 0, then the team's points will always add up to 7
    if (max_ind == 0) {
        do {
            var third = Math.floor(Math.random() * (max - min + 1)) + min;
            ch3p = chlist[third]['points']
        }
        while (third == 35 || third == id1 || third == id2 || p1 + p2 + ch3p !== 7);
    } else {
        do {
            var third = Math.floor(Math.random() * (max - min + 1)) + min;
            ch3p = chlist[third]['points']
        }
        while (third == 35 || third == id1 || third == id2 || ch3p > 7 - p1 - p2);
    }
    return third;
}


// Generate assist
// Will pick a number from 0 to 2 then will pick that iteration in the list
function genAssist() {
    var assists = ['assist_1', 'assist_2', 'assist_3'];
    var rand_assist = Math.floor(Math.random() * assists.length);
    return assists[rand_assist];
}


// Generate team
function genTeam(max_ind) {
    // Get data
    var all_characters = JSON.parse(characters);
    // First character
    var first = genChar1();
    var ch1 = all_characters[first];
    var ch1_name = ch1.name;
    var ch1_points = ch1.points;
    var ch1_assist = ch1[genAssist()];
    // Second character
    var second = genChar2(all_characters, first, ch1_points);
    var ch2 = all_characters[second];
    var ch2_name = ch2.name;
    var ch2_points = ch2.points;
    var ch2_assist = ch2[genAssist()];
    // Third character
    var third = genChar3(all_characters, first, ch1_points, second, ch2_points, max_ind);
    var ch3 = all_characters[third];
    var ch3_name = ch3.name;
    var ch3_points = ch3.points;
    var ch3_assist = ch3[genAssist()];
    // Sum all points
    const arr = [ch1_points, ch2_points, ch3_points];
    const reducer = (a, b) => a + b;
    var total_points = arr.reduce(reducer);
    // Input text in labels
    var char1 = document.getElementById('char1');
    var char2 = document.getElementById('char2');
    var char3 = document.getElementById('char3');
    var total = document.getElementById('total');
    char1.innerHTML = [ch1_name, ch1_assist].join(', ');
    char2.innerHTML = [ch2_name, ch2_assist].join(', ');
    char3.innerHTML = [ch3_name, ch3_assist].join(', ');
    total.innerHTML = 'TOTAL POINTS: ' + total_points;
}

