// function test() {
//     console.log('this function has been hit');
//     document.getElementById('test').innerHTML = 'another test???';
// }

angular
    .module('app', []);

angular
    .module('app')
    .controller('controllerT', controllerT)

function controllerT() {
    var vm = this;
    vm.test = 'second';
}