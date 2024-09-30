const bar = document.querySelector('.menu')
const dropbar = document.querySelector('.dropbar-main')
const tap = document.querySelectorAll('.sod')

bar.addEventListener('click',()=>{
    dropbar.style.display = dropbar.style.display === 'none' ? 'block' : 'none'
})
tap.forEach(taps => {
    taps.addEventListener('click',()=>{
        dropbar.style.display = 'none'
    })
});
document.querySelector('.dropbar-login').addEventListener('click', (e)=>{
   e.preventDefault()
})

document.querySelector('.submit').addEventListener('click', (e)=>{
    e.preventDefault()
})