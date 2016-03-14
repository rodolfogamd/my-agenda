stage { 'first':
    before => Stage['main'],
}

node default {
    
    class { 'system':
        stage => first
    }

    class { 'language':
        stage => main
    }
    ->
    class { 'webserver':
        stage => main
    }
    ->
    class { 'database':
        stage => main
    }
    
}