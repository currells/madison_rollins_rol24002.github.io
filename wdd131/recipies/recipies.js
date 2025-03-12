// Import recipies from the .mjs file
import './recipies.mjs'

// create math function ro generate random numb
function random(num){
    return Math.floor(Math.random() * num);
}

//function pulling a random recipie based on generated numb
function getRandomRecipie(list){
    const listLength = list.length;
	const randomNum = random(listLength);
	return list[randomNum];
}


// to test
console.log(getRandomListEntry(recipes));