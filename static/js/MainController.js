angular
    .module('app')
    .controller('MainController', MainController)

function MainController() {
    var vm = this;
    vm.test = 'from main controller';
    vm.moveArm = function() {
        console.log('I have been hit!!!');
    }
}