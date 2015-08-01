var gulp = require('gulp');
var gutil = require('gulp-util');
var bower = require('bower');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');
var sh = require('shelljs');
var uglify  = require('gulp-uglify');

var paths = {
  sass: ['./scss/*/*.scss', './scss/*.scss'],
  uglify: ['./js/*/*.js', './js/*.js'],
  html: ['./templates/*/*.html', './templates/*.html'],
  img: ['./img/*/*.*', './img/*.*']
};

gulp.task('default', ['sass', 'uglify', 'html', 'img']);

gulp.task('sass', function(done) {
  gulp.src(paths.sass)
    .pipe(sass({
      errLogToConsole: true
    }))
    .pipe(minifyCss({
      keepSpecialComments: 0
    }))
    .pipe(rename({ extname: '.min.css' }))
    .pipe(gulp.dest('../../static/mobile/css'))
    .on('end', done);
});

gulp.task('uglify', function () {
  gulp.src(paths.uglify)
      .pipe(uglify())
      .pipe(rename({extname: '.min.js'}))
      .pipe(gulp.dest('../../static/mobile/js'));
});

gulp.task('html', function(){
    gulp.src(paths.html)
        .pipe(gulp.dest('../../templates/mobile'))
});

gulp.task('img', function(){
    gulp.src(paths.img)
        .pipe(gulp.dest('../../static/mobile/img'))
});

gulp.task('watch', function() {
  gulp.watch(paths.sass, ['sass']);
  gulp.watch(paths.uglify, ['uglify']);
  gulp.watch(paths.html, function(){
    gulp.run('default');
  });
});

gulp.task('install', ['git-check'], function() {
  return bower.commands.install()
    .on('log', function(data) {
      gutil.log('bower', gutil.colors.cyan(data.id), data.message);
    });
});

gulp.task('git-check', function(done) {
  if (!sh.which('git')) {
    console.log(
      '  ' + gutil.colors.red('Git is not installed.'),
      '\n  Git, the version control system, is required to download Ionic.',
      '\n  Download git here:', gutil.colors.cyan('http://git-scm.com/downloads') + '.',
      '\n  Once git is installed, run \'' + gutil.colors.cyan('gulp install') + '\' again.'
    );
    process.exit(1);
  }
  done();
});
