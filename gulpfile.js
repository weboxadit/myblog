var gulp = require('gulp'),
	uglify = require('gulp-uglify'),
	sass = require('gulp-ruby-sass'),
	plumber = require('gulp-plumber');


// error handling function
function errorLog(error){
	console.error.bind(error)
	this.emit('end');
}

// scripts task
// uglifies

gulp.task('scripts',function(){
	gulp.src('static/blog/js/**/*.js')
		.pipe(uglify())
		.on('error',errorLog)
		.pipe(gulp.dest('destination/blog/js'))
});

// styles

gulp.task('styles',function(){

	return sass('static/blog/css/**/*.scss',{
		style: 'compressed'
		})
		.on('error',errorLog)
  		.pipe(gulp.dest('destination/blog/css'))
});

// watch task
// watches javascript
gulp.task('watch',function(){
	gulp.watch('static/blog/js/*.js',['scripts']);
	gulp.watch('static/blog/css/**/*.scss',['styles']);
});

gulp.task('default',['scripts','styles','watch']);

