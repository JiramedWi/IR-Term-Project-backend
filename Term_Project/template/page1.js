console.log("page 1 script");

const handleFormSubmit = (event) => {
	event.preventDefault();
	console.log("page 1 form submit");
	var query = document.getElementById("query").value;
	var score = document.getElementById("ranking").value;
	var raw = "";

	var requestOptions = {
		method: 'POST',
		body: raw,
		redirect: 'follow'
	};
	fetch(
		"http://127.0.0.1:5000/query?query="+query+"&score="+score+""
		, requestOptions)
		.then((response) => response.json())
		.then((result) => {
			console.log('query :', query)
			console.log('query :', score)
			console.log("http://127.0.0.1:5000/query?query=" + query + "&score=" + score + "")
			//NOTE: for the real data, you should use variable 'result' to loop display data
			console.log("result", result);
			let res = "";

			result.forEach((item) => {
				console.log("item", item);

				res += `<div class="card">
			    <div class="card-header">
			        <div class="card-sub-header">
			         <p class="artist">${item.artist}</p>
			         <p class="song">${item.song}</p>
			        </div>
			         <p class="rank">${item.rank}</p>
			     </div>
			     <p class="lyric">${item.lyric}</p></div>`;
			});

			console.log("res", res);
			document.getElementById("page1-result-box").innerHTML = res;
		})
		.catch((error) => console.log("error", error));
};

