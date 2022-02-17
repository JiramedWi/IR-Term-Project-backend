console.log("page 2 script");

const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log("page 2 form submit");
    var query = document.getElementById("query").value;

    var raw = "";

    var requestOptions = {
        method: 'POST',
        redirect: 'follow'
    };
    fetch(
        "http://127.0.0.1:5000/search?query=" + query + "", requestOptions)
        .then((response) => response.json())
        .then((result) => {
            console.log('query :', query)

            console.log("http://127.0.0.1:5000/search?query=" + query + "")
            //NOTE: for the real data, you should use variable 'result' to loop display data
            console.log("result", result);
            let res = "";

            result.forEach((item) => {
                console.log("item", item);

                res += `<div class="card">
			    <div class="card-header">
			        <div class="card-sub-header">
			         <p class="artist">${item.Artist}</p>
			         <p class="song">${item.Song}</p>
                     </div>
			     </div>
			     <p class="lyric">${item.Lyric}</p></div>`;
            });

            console.log("res", res);
            document.getElementById("page2-result-box").innerHTML = res;
        })
        .catch((error) => console.log("error", error));
};

