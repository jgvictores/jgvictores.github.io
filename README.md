<style>
  .ascii-banner-container {
    width: 100%;
    overflow: hidden;
    margin-top: -20px;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    user-select: none;
  }

  #ascii-cat {
    font-family: "Ubuntu Mono", Consolas, "Courier New", Courier, monospace;
    font-size: 16px;
    line-height: 1.2;
    white-space: pre;
    color: #333333;
    margin: 0;
    padding: 0;
    background: transparent;
    border: none;
    overflow: hidden; /* OVERRIDES THE THEME'S SCROLLBAR */
  }

  /* Dark Mode Support */
  @media (prefers-color-scheme: dark) {
    #ascii-cat {
      color: #f2f2f2; 
    }
  }
</style>

<div class="ascii-banner-container">
  <pre id="ascii-cat"></pre>
</div>

<script>
  (function() {
    const frames = [];
    const numFrames = 88;
    
    for (let i = 0; i < numFrames; i++) {
      let c1 = "       /\\_/\\   ";
      let c2 = Math.floor(i / 2) % 2 === 0 ? "      ( o.o )  " : "      ( >.< )  ";
      let c3 = Math.floor(i / 2) % 2 === 0 ? "  ~~~~-----    " : "   ~~~-----    ";
      let c4 = Math.floor(i / 2) % 2 === 0 ? "____//____\\\\___" : "____\\\\____//___";

      let state = i % 4;
      let y3 = (state === 3) ? "  -\\ " : " /-\\ ";
      let y4 = (state === 1) ? " \\-  " : (state === 2) ? "  -/ " : " \\-/ ";

      let midSpace = "        ";
      let midTrail = "________";
      let endSpace = " ".repeat(60);
      let endTrail = "        " + "_".repeat(52); 

      let base_l1 = c1 + midSpace + "     " + endSpace;
      let base_l2 = c2 + midSpace + "     " + endSpace;
      let base_l3 = c3 + midSpace + y3 + endSpace;
      let base_l4 = c4 + midTrail + y4 + endTrail;

      let l1, l2, l3, l4;
      if (i > 0) {
        l1 = base_l1.slice(-i) + base_l1.slice(0, -i);
        l2 = base_l2.slice(-i) + base_l2.slice(0, -i);
        l3 = base_l3.slice(-i) + base_l3.slice(0, -i);
        l4 = base_l4.slice(-i) + base_l4.slice(0, -i);
      } else {
        l1 = base_l1; l2 = base_l2; l3 = base_l3; l4 = base_l4;
      }

      let fullText = l1.repeat(3) + "\n" + l2.repeat(3) + "\n" + l3.repeat(3) + "\n" + l4.repeat(3);
      frames.push(fullText);
    }

    const orderedFrames = frames.slice(60).concat(frames.slice(0, 60));
    
    let currentFrame = 0;
    const catElement = document.getElementById('ascii-cat');
    
    // SLOWED DOWN: Interval increased from 100 to 200 ms
    setInterval(() => {
      catElement.textContent = orderedFrames[currentFrame];
      currentFrame = (currentFrame + 1) % numFrames;
    }, 200); 
  })();
</script>

### Universidad Carlos III de Madrid (UC3M)

- Associate Professor at [UC3M](https://www.uc3m.es)
- Researcher in Robotics and AI at [RoboticsLab (UC3M)](https://roboticslab.uc3m.es/author/jcgvicto)
- Robotics Society Collaborator at [ASROB (UC3M)](https://asrob.uc3m.es)
- Coordinador Grupo Temático de Robótica (GTRob) at [Comité Español de Automática (CEA)](https://www.ceautomatica.es/robotica)
- PhD in Electrical Engineering, Electronics and Automation
- [CV (html)](cv/JuanGVictoresCV.html) / [CV (pdf)](cv/JuanGVictoresCV.pdf)
