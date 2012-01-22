
/*
 * GET home page.
 */

exports.index = function(req, res){
	res.render('index', { title: 'Index' })
};

exports.demos = function(req, res){
	res.render('demos', { title: 'Demos' })
}

exports.socketio_demo = function(req, res){
	res.render('socketio_demo', { title: 'Socket.io Demo' })
}
