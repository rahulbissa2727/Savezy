const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
async function pick_zepto(name, weight, id) {
  if (!name || !weight || !id) {
    return [];
  }

  // Send a request to the Zepto API with the name and weight parameters
  const url = 'https://www.zeptonow.com/search';
  const query = `${name} ${weight} grams`;
  const params = { query };
  const response = await axios.get(url, { params });

  // Parse the response to extract the relevant information
  const results = [];
  if (response.status === 200) {
    const $ = cheerio.load(response.data);
    fs.writeFile('response_node.html', response.data, (err) => {
        if (err) throw err;
        console.log('HTML content saved to response.html');
      });
    const grid = $('div._3dNoiD');
    if (grid.length === 0) {
      console.error('Error: Could not find grid element');
      return [];
    }
    const items = grid.find('div.rO1D6k');
    items.slice(0, 10).each((i, item) => {
      const name = $(item).find('div.vhtkim').text().trim();
      const weight = $(item).find('div.j7HcYM').text().trim();
      const price = $(item).find('div.j7HcYM').next().text().trim();
      const result = { name, weight, price };
      results.push(result);
    });
  }

  return results;
}

// Example usage
(async () => {
  const results = await pick_zepto('coffee', 250, '123');
  console.log(results);
})();