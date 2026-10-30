// Hiện dần các khối khi cuộn tới. Không có JS thì mọi thứ vẫn hiện sẵn (class "js" do chính file này thêm).
document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    }
  }, { rootMargin: '0px 0px -10% 0px' });
  items.forEach((el) => io.observe(el));
});
