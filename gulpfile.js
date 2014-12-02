/*
    gulfile.js
*/

var gulp   = require('gulp'),
    uglify = require('gulp-uglify'),
    sass   = require('gulp-ruby-sass');


gulp.task('scripts', function() {
   gulp.src('./core/static/assets/scripts/*.js')
       .pipe(uglify())
       .pipe(gulp.dest('./core/static/js'));
});

gulp.task('styles', function() {
    gulp.src('./core/static/assets/sass/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./core/static/css'));
});

gulp.task('watch', function() {
    gulp.watch('./core/static/assets/sass/**/*.scss', [ 'styles', ]);
});

gulp.task('default', [ 'scripts', 'watch', ]);