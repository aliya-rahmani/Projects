// NOTE: This is file runs with the Deno runtime

var gh_username = Deno.args[0]; // Name should be provided as the command line agruments
const resp = await fetch(`https://api.github.com/users/${gh_username}`); // Get the response
var json_resp = await (resp).json(); // Get the JSON

const avatar_url = json_resp["avatar_url"]; // The avatar is present on this link
const avatar_data = await fetch(avatar_url); // Fetch it from the URL
const data_blob = await (avatar_data).blob(); // Get the blob from data
const image_data = await(data_blob).stream().getReader().read(); // Read the data from the stream's blob
const value = image_data.value; // The actual value to be written to the file
Deno.writeFileSync(`${gh_username}.png`, value); // Writing it!!

// Obfuscated version
// (await fetch(`https://api.github.com/users/${Deno.args[0]}`)).json().then( async (json) => { Deno.writeFileSync(Deno.args[0]+".png",(await (await (await fetch(json["avatar_url"])).blob()).stream().getReader().read()).value); } )