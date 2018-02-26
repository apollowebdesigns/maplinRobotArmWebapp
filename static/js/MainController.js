(function() {
    angular
        .module('app')
        .controller('MainController', MainController);

    function MainController() {
        var vm = this;

        vm.test = 'hello from the test!!!!';
    }
})();