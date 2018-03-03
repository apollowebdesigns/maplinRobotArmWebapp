angular
    .module('app')
    .controller('MainController', MainController)

MainController.$inject = ['$http', '$log'];

function MainController($http, $log) {
    var vm = this;
    vm.test = 'from main controller';
    vm.moveArm = (url) => {
        $log.info('I have been hit!!!');
        $http
            .get("/arm/" + url)
            .then(response => console.log(response));
    }
}