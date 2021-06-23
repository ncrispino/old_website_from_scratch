// Goal: Toggle between most recent project/post on home page

document.getElementById('toggle').value = 'Click to see most recent post';
document.getElementById('show-proj').style.display = 'block';

function show() {
  // alert('button pressed');
  let disp_post = document.getElementById('show-post');
  let disp_proj = document.getElementById('show-proj');
  // alert(disp_post);
  if (disp_proj.style.display == 'block') {
    disp_post.style.display = 'block';
    disp_proj.style.display = 'none';
    document.getElementById('toggle').value = 'Click to see most recent project';
  }
  else {
    disp_post.style.display = 'none';
    disp_proj.style.display = 'block';
    document.getElementById('toggle').value = 'Click to see most recent post';
  }
}
