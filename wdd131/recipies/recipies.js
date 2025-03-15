// Import recipies from the .mjs file
import { recipes } from './recipies.mjs';

print(recipes);

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

// function to generate tags HTML
function tagsTemplate(tags) {
    return tags.map(tag => `<li>${tag}</li>`).join('');
}

// function to generate rating HTML
function ratingTemplate(rating) {
    let html = `<span
    class="rating"
    role="img"
    aria-label="Rating: ${rating} out of 5 stars"
    >`;
    
    for (let i = 1; i <= 5; i++) {
        if (i <= rating) {
            html += `<span aria-hidden="true" class="icon-star">⭐</span>`;
        } else {
            html += `<span aria-hidden="true" class="icon-star-empty">☆</span>`;
        }
    }
    
    html += `</span>`;
    return html;
}

//recipie templates
function recipeTemplate(recipe) {
    return `<figure class="recipe">
    <img src="${recipe.image}" alt="image of ${recipe.name}" />
    <figcaption>
        <ul class="recipe__tags">
            ${tagsTemplate(recipe.tags)}
        </ul>
        <h2><a href="#">${recipe.name}</a></h2>
        <p class="recipe__ratings">
            ${ratingTemplate(recipe.rating)}
        </p>
        <p class="recipe__description">
            ${recipe.description}
        </p>
    </figcaption>
    </figure>`;
}

// render recipes
function renderRecipes(recipeList) {
    // get the element we will output the recipes into
    const recipeContainer = document.getElementById('recipe');

    // use the recipeTemplate function to transform our recipe objects into recipe HTML strings
    const recipesHTML = recipeList.map(recipe => recipeTemplate(recipe)).join('');

    // Set the HTML strings as the innerHTML of our output element.
    recipeContainer.innerHTML = recipesHTML;
}

//filter
function filterRecipes(query) {
    return recipes.filter(recipe => {
        const lowerCaseQuery = query.toLowerCase();
        return (
            recipe.name.toLowerCase().includes(lowerCaseQuery) ||
            recipe.description.toLowerCase().includes(lowerCaseQuery) ||
            recipe.tags.find(tag => tag.toLowerCase().includes(lowerCaseQuery)) ||
            recipe.recipeIngredient.find(ingredient => ingredient.toLowerCase().includes(lowerCaseQuery))
        );
    }).sort((a, b) => a.name.localeCompare(b.name));
}

//search hadleras
function searchHandler(event) {
    event.preventDefault();
    const query = document.getElementById('search-input').value.toLowerCase();
    const filteredRecipes = filterRecipes(query);
    renderRecipes(filteredRecipes);
}

//event listhererw for search
document.getElementById('search-form').addEventListener('click', searchHandler);

function init() {
    // get a random recipe
    const recipe = getRandomRecipie(recipes);
    // render the recipe with renderRecipes.
    renderRecipes([recipe]);
}

init();


// to test
const recipe = getRandomListEntry(recipes);
console.log(recipeTemplate(recipe));