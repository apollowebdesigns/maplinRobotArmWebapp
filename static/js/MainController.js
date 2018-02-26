angular
    .module('app')
    .controller('MainController', MainController);

MainController.$inject = ['$scope']

function MainController() {

    console.log('hit hit')
    $scope.test = 'hello from the test!!!!';
}