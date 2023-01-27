/*function reload(){
$.getJSON('http://10.0.120.9/getUsbList.json', function(data) {
    let usbSlot="";
    for(let i=0;i<data.length;i++){
        if(data[i].FileCount>0){
            if(data[i].status=="nocheck"){
                usbSlot+="<div class='usb'>"+'Initializing Device...'+"</div>";
            }else if(data[i].status=="scanning"){
                let percentage=0;
                let lines=[];
                let fileCounter="";
                if(data[i].result.length>5){
                    let lines=data[i].result.split("\n")
                    lines=lines.length;
                    
                    percentage=Math.floor(lines*100/(data[i].FileCount+3));

                    fileCounter=lines+" from "+(data[i].FileCount+3);
                }

                if(percentage<=98){
                    usbSlot+="<div class='usb in-progress'>"+'Processing ('+percentage+'% / 100%) '+"</div>";
                }else
               {   usbSlot+="<div class='usb in-progress-summary'>"+'Generating Summary...'+"</div>";
            }
            }else if(data[i].status=="finish"){
               
                let textResult=data[i].result;
                let seperated=textResult.split("----------- SCAN SUMMARY -----------");
                let files=seperated[0];
                let summary=seperated[1];
                summary=summary.replace("\n","");
                console.log(summary);
                summary=summary.replace(/\n/g,'\\n').replace(/\t/,'\\t');
                let lines=summary.split("\\n");
                let infected=0;
                for(a=0;a<lines.length;a++){
                    let b=lines[a].split("Infected files:");
                    if(b.length>1 && b[0].length==0){
                        infected=parseInt(b[1]);
                    }
                }
                if(infected==0){
                 usbSlot+="<div class='usb finish'>"+'Finished'+"</div>";
                }else{
                    usbSlot+="<div class='usb finish alert'>"+'Infection Found'+"</div>";    
                    usbSlot+="<div class='actions'>"+'<button>Details</button><button>Remove all infected files</button>'+"</div>";    
                    
                }
                //usbSlot+="<div class='summary'>";
                for(a=0;a<lines.length;a++){
                  //  usbSlot+="<p>"+lines[a]+"</p>";
                }
              // usbSlot+="</div>";
            }
        }else{
            usbSlot+="<div class='usb-empty'> Empty </div>";
        }
    }
    $("#usb-list").html(usbSlot);
  });
  setTimeout(reload,1000)
}

reload()
*/