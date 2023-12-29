// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
} else {
  alert('The File APIs are not fully supported in this browser.');
}

function readSingleFile(evt) {
   
    var f = evt.target.files[0]; 

    if (f) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var result = e.target.result;
            //console.log(result)
            document.getElementById('text').value=result;
      }
      r.readAsText(f,'CP1251');
    } else { 
      alert("Failed to load file");
    }
  }

  document.getElementById('file').addEventListener('change', readSingleFile, false);
///////////////////////////////////////////////////////////////////////////////////

//Для docx
        (function() {
    document.getElementById("file")
        .addEventListener("change", handleFileSelect, false);
        
    function handleFileSelect(event) {
        readFileInputEventAsArrayBuffer(event, function(arrayBuffer) {
            mammoth.extractRawText({arrayBuffer: arrayBuffer})
                .then(displayResult)
                .done();
        });
    }
    
    function displayResult(result) {
        document.getElementById("text").value = result.value;
  
    }
    
    function readFileInputEventAsArrayBuffer(event, callback) {
        var file = event.target.files[0];

        var reader = new FileReader();
        
        reader.onload = function(loadEvent) {
            var arrayBuffer = loadEvent.target.result;
            callback(arrayBuffer);
        };
        
        reader.readAsArrayBuffer(file);
    }

    function escapeHtml(value) {
        return value
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }
})();







