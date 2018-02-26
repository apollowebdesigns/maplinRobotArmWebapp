angular
    .module('app')
    .controller('MainController', MainController);

function MainController() {
    var vm = this;


    console.log('hit hit')
    vm.test = 'hello from the test!!!!';
}