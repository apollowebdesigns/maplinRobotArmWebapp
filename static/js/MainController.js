angular
    .module('app')
    .controller('MainController', MainController);

MainController.$inject = ['$scope'];

function MainController($scope) {

    var vm = this;

    console.log('hit hit')
    vm.test = 'hello from the test!!!!';

    $scope.second = 'try again';
}