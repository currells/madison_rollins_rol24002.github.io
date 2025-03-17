// Import recipies from the .mjs file
import recipes from './recipes.mjs';


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
    if (Array.isArray(tags)) {
        return tags.map(tag => `<li>${tag}</li>`).join('');
    } else {
        return ''; // Return an empty string or some default value
    }
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
        <div class="recipe-info">
            <ul class="recipe__tags">
               ${tagsTemplate(recipe.tags)}
            </ul>
            <h2 class="recipe-name"><a href="#">${recipe.name}</a></h2>
            <p class="rating">
                ${ratingTemplate(recipe.rating)}
            </p>
            <p class="recipe__description">
                ${recipe.description}
            </p>
        </div>
    </figcaption>
    </figure>`;
}

// render recipes
function renderRecipes(recipeList) {
    const recipeContainer = document.getElementById('recipe');

    if (recipeList.length === 0) {
        recipeContainer.innerHTML = "<p>No recipes matching your search.</p>";
    } else {
        const recipesHTML = recipeList.map(recipe => recipeTemplate(recipe)).join('');
        recipeContainer.innerHTML = recipesHTML;
    }
}

//filter
function filterRecipes(query) {
    return recipes.filter(recipe => {
        const lowerCaseQuery = query.toLowerCase();
        return (
            recipe.name.toLowerCase().includes(lowerCaseQuery) ||
            recipe.description.toLowerCase().includes(lowerCaseQuery) ||
            (Array.isArray(recipe.tags) && recipe.tags.find(tag => tag.toLowerCase().includes(lowerCaseQuery)))
        );
    }).sort((a, b) => a.name.localeCompare(b.name));
}

//search hadleras
function searchHandler(event) {
    event.preventDefault();
    const query = document.getElementById('search-input').value.toLowerCase();
    console.log("Search Query:", query);

    const filteredRecipes = filterRecipes(query);
    console.log("Filtered Recipes:", filteredRecipes);

    renderRecipes(filteredRecipes);
}


//event listhererw for search
document.getElementById('search-form').addEventListener('submit', searchHandler);

function init() {
    // get a random recipe
    const recipe = getRandomRecipie(recipes);
    // render the recipe with renderRecipes.
    renderRecipes([recipe]);
}

init();



// to test
//const recipe = getRandomListEntry(recipes);
console.log(recipeTemplate(recipe));