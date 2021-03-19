const $button=$("#guess-button");
const $guess=$("#guess");
const $message=$("#response");
const $score=$("#score");
let score=0;
let sec=0;

function timer(){
    sec++;
    console.log(sec);  
    if(sec>=60){
        clearInterval(start);
        endGame();   
    }          
}
 start= setInterval(timer, 1000);

async function handleGuess(evt){
    evt.preventDefault();
    const check= await axios.get("/check-word",{
        params:{guess: $guess.val().toLowerCase()}        
    })
    let result=check.data.result;
    console.log(result);
    
    if(result==="ok"){
        $message.text("ok");
        console.log("in iff");
        updateScore(result);
    }
    else if(result==="not-on-board"){
        $message.text("not on board");
        console.log("in iff");
    }
    else if(result==="not-word"){
        $message.text("not a word");
        console.log("in iff");
    }
}

$button.on("click", handleGuess);

function updateScore(result){
    score+=result.length;
    console.log(score);
    $score.text(`${score}`)
}

async function endGame(){
    $message.text("game over");
    const sendScore=await axios.post("/save-score",{        
            score:score        
    })

    console.log(await sendScore.data)

    

}
