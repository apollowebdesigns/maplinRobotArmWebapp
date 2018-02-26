(function() {
    angular
        .module('app')
        .controller('MainController')

    function MainController() {
        var vm = this;

        vm.test = 'hello from the test!!!!';
    }
})();