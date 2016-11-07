var chart = c3.generate({
    data: {
        // iris data from R
        columns: [
            ['Feito', 22.74],
            ['A Fazer', 100 - 22.74],
        ],
        type : 'pie',
        onclick: function (d, i) { console.log("onclick", d, i); },
        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
        onmouseout: function (d, i) { console.log("onmouseout", d, i); },
        colors: {
        	'Feito': "#ff0000",
          'A Fazer': "#0aa955",
      	}
    }
    
});