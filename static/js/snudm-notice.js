var n = noty({
    layout: 'topRight',
    theme: 'relax',
    text: '<strong>[데이터마이닝 연구실 연말 연구활동 성과]</strong><br>- 안진원, 류성원 NIPS Workshop 발표<br>- 김은지, 최민 KDMS 최우수논문상 수상<br>- 강연국 AAAI 발표<br><a href="/ko/notices/20181203" class="pull-right">[바로가기]</a>',
    animation: {
        open: 'animated bounceInDown',
        close: {height: 'toggle'}, // jQuery animate function property object
        easing: 'swing', // easing
        speed: 500 // opening & closing animation speed
    }
});
