<?php

use Cleveraluminate\Foundation\Inspiring;
use Cleveraluminate\Support\Facades\Artisan;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');
